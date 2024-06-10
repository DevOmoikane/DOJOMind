import java.util.Scanner;

public class MainApp {
    public static String RGBToHex(int r, int g, int b) {
        return String.format("#%02X%02X%02X", r, g, b);
    }

    public static String RGBToHex(String rgb) {
        String[] rgbValues = rgb.split(",");
        try {
            int r = Integer.parseInt(rgbValues[0].trim());
            int g = Integer.parseInt(rgbValues[1].trim());
            int b = Integer.parseInt(rgbValues[2].trim());
            return RGBToHex(r, g, b);
        } catch (NumberFormatException e) {
            System.out.println("Invalid input");
        }
        return null;
    }

    public static void main(String[] args) {
        System.out.println("Enter the value of R, G, B: ");
        Scanner input = new Scanner(System.in);
        String inputString = input.nextLine();
        System.out.println("Color in hex is: " + RGBToHex(inputString));
    }
}
