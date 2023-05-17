import java.io.*;
import java.util.*;

class PayOutOFBoundsException extends Exception{

public PayOutOFBoundsException(String st){super(st);}}

public class PaymentException {
    public static void main(String[] args) throws PayOutOFBoundsException {
            Scanner in = new Scanner(System.in);
            System.out.println("Enter your Salary:- ");
            int sal = in.nextInt();
            if(sal<8000){
                throw new PayOutOFBoundsException("Salary out of bounds less than 8000");
            }else{
                System.out.println("");
                Double da = sal * 0.02;
                Double hra = sal * 0.20;
                Double ca = sal * 0.05;
                Double ta = sal * 0.04;
                Double proftax = sal * 0.10;
                System.out.println("Gross salary = "+((sal+da+hra+ca+ta)-proftax));
            }
	}
}

