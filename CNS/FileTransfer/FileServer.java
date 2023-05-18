package FileTransfer;
import java.io.*;
import java.net.*;

public class FileServer {
    public static void main(String[] args) throws Exception {
        ServerSocket ss = new ServerSocket(5000);
        Socket socket = ss.accept();
        File file = new File("data.txt");
        FileInputStream fis = new FileInputStream(file);
        BufferedInputStream bis = new BufferedInputStream(fis);

        OutputStream os = socket.getOutputStream();

        byte[] contents;
        long fl = file.length();
        long current = 0;
        while (current != fl) {
            int size = 10000;
            if (fl - current >= size)
                current += size;
            else {
                size = (int) (fl - current);
                current = fl;
            }
            contents = new byte[size];
            bis.read(contents, 0, size);
            os.write(contents);
            System.out.println("Sending file..." + (current * 100) / fl + "% complete");
        }

        os.flush();
        bis.close();
        socket.close();
        ss.close();
        System.out.println("File sent successfully");
    }
}