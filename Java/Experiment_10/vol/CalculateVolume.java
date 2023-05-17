package Java.Experiment_10.vol;

public class CalculateVolume //first go to the vol directory in the terminal and then type javac Cylinder.java CalculateVolume.java to compile them and then move out of the java folder to the Sem4exps folder in the terminal and then execute by typing java Java.Experiment_10.vol.CalculateVolume, we have to do this because we have defined the package in the program
{
    public static void main(String[] args) {
        double radius = 3.5;
        double height = 10.0;

        Cylinder cylinder = new Cylinder(radius, height);
        double volume = cylinder.volume();

        System.out.println("Volume of the cylinder: " + volume);
    }
}
