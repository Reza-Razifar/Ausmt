
// Test is done in Intellij via JUnit

/**
 * A static class contain for doing mathematically operations.
 */
public class Calculator {
    private Calculator(){}
    static double sum(double a, double b){
        return a + b;
    }

    static double multiply(double a, double b){
        if(a == 0){
            return -1;
        }
        return a * b;
    }
}
