abstract class Shape {
    double area; 
    abstract void findArea();
    abstract void displayArea();
    void getDimensions(double dimensions) {
    }
}
class Circle extends Shape {
    double radius; 
    void findArea() {
        area = Math.PI * radius * radius;
    }
    void displayArea() {
        System.out.println("Area of Circle: " + area);
    }
    void getDimensions(double dim1, double dim2) {
            radius = dim1;
    }
}
class Triangle extends Shape {
    double base; 
    double height;
    void findArea() {
        area = 0.5 * base * height;
    }
    void displayArea() {
        System.out.println("Area of Triangle: " + area);
    }
    void getDimensions(double dim1, double dim2) {
            base = dim1;
            height = dim2;
    }
}
class Rectangle extends Shape {
    private double length; 
    private double breadth; 
    void findArea() {
        area = length * breadth;
    }
    void displayArea() {
        System.out.println("Area of Rectangle: " + area);
    }
    void getDimensions(double dim1, double dim2) {
            length = dim1;
            breadth = dim2;
    }
}

// Driver class
public class ShapeAbstraction {
    public static void main(String[] args) {
        Circle circle = new Circle();
        Triangle triangle = new Triangle();
        Rectangle rectangle = new Rectangle();

        circle.getDimensions(5.0,0.0);
        triangle.getDimensions(10.0, 6.0); 
        rectangle.getDimensions(8.0, 4.0);

        circle.findArea();
        circle.displayArea();

        triangle.findArea();
        triangle.displayArea();

        rectangle.findArea();
        rectangle.displayArea();
    }
}

