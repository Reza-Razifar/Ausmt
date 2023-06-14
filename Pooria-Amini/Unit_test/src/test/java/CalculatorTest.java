import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class CalculatorTest {

    @Test
    @DisplayName("Add two numbers")
    void sum() {
        assertEquals(4, Calculator.sum(2, 2));
    }

    @Test
    @DisplayName("Multiply two numbers")
    void multiply() {
        assertAll(
                ()-> assertEquals(8, Calculator.multiply(4, 2)),
                ()-> assertEquals(-20, Calculator.multiply(4, -5)),
                ()-> assertEquals(0, Calculator.multiply(0, 5)),
                ()-> assertEquals(0, Calculator.multiply(5, 0))
        );
    }
}