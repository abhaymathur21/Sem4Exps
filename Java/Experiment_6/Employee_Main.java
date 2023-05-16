class Employee {
    double salary;
    double basic, hra, ta;

    Employee(double basic, double hra) {
        this.basic = basic;
        this.hra = hra;
    }

}
class basic_sal extends Employee
{
    double gross;

    basic_sal(double basic,double hra)
    {
        super(basic,hra);
        ta=0.01*basic;

    }
    double calsal()
    {
        gross=basic+hra+ta;

        return gross;
    }


}
class Employee_Main
{
    public static void main(String [] args)
    {
        Employee e1=new Employee(200000,5.5606000);
        basic_sal b1=new basic_sal(200000,5.5606000);
        System.out.println("Salary is:"+b1.calsal());
    }
}

