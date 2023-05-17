import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

class LoginEvent extends JFrame implements ActionListener
{
    JFrame jf;
    JLabel l1;
    JTextField tf1;
    JButton b1,b2;

    LoginEvent()
    {
        jf = new JFrame("Login Test");
        tf1 = new JTextField(5);
        l1= new JLabel("Enter number");
        b1 = new JButton("Find Factorial");
        b2 = new JButton("Reset");
        jf.setLayout(new FlowLayout());
        jf.add(l1);
        jf.add(tf1);
        jf.add(b1);
        jf.add(b2);
        b1.addActionListener(this);
        b2.addActionListener(this);
        jf.setSize(500, 100);
        jf.setVisible(true);
    }

    public void actionPerformed(ActionEvent e)
    {
        if(e.getSource() == b1)
        {
            int s1 = Integer.parseInt(tf1.getText());
            int fact = 1;
            for(int i = 1; i <= s1; i++)
            {
                fact*=i;
            }
            System.out.println("Factorial is " + fact);
        }
        else if(e.getSource() == b2)
        {
            tf1.setText("");
        }
    }

    public static void main(String[] args)
    {
        LoginEvent x = new LoginEvent();
    }
}