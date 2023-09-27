import seminars.first.model.Calculator;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

public class CalculatorTest {
    public static void main(String[] args) {
        // Проверка базового функционала с целыми числами:
//        if (8 != Calculator.calculation(2, 6, '+')) {
//            throw new AssertionError("Ошибка в методе");
//        }
//
//        if (0 != Calculator.calculation(2, 2, '-')) {
//            throw new AssertionError("Ошибка в методе");
//        }
//
//        if (14 != Calculator.calculation(2, 7, '*')) {
//            throw new AssertionError("Ошибка в методе");
//        }
//
//        if (2 != Calculator.calculation(100, 50, '/')) {
//            throw new AssertionError("Ошибка в методе");
//        }
//
//        // Случаи с неправильными аргументами
//        // аргумент operator типа char, должен вызывать исключение, если он получает не базовые символы (+-*/)
//        try {
//            Calculator.calculation(8, 4, '_');
//        } catch (IllegalStateException e) {
//            if (!e.getMessage().equals("Unexpected value operator: _")) {
//                throw new AssertionError("Ошибка в методе");
//            }
//        }

        // Проверка базового функционала с целыми числами, с использованием утверждений:
        assert 8 == Calculator.calculation(2, 6, '+');
        assert 0 == Calculator.calculation(2, 2, '-');
        assert 14 == Calculator.calculation(2, 7, '*');
        assert 2 == Calculator.calculation(100, 50, '/');

        // Проверка базового функционала с целыми числами, с использованием утверждений AssertJ:
        assertThat(Calculator.calculation(2, 6, '+')).isEqualTo(8);
        assertThat(Calculator.calculation(-2, -6, '+')).isEqualTo(-8);
        assertThat(Calculator.calculation(2, -6, '+')).isEqualTo(-4);
        assertThat(Calculator.calculation(-2, 6, '+')).isEqualTo(4);
        assertThat(Calculator.calculation(2, 2, '-')).isEqualTo(0);
        assertThat(Calculator.calculation(-2, -2, '-')).isEqualTo(0);
        assertThat(Calculator.calculation(-2, 2, '-')).isEqualTo(-4);
        assertThat(Calculator.calculation(2, -2, '-')).isEqualTo(4);
        assertThat(Calculator.calculation(2, 7, '*')).isEqualTo(14);
        assertThat(Calculator.calculation(-2, -7, '*')).isEqualTo(14);
        assertThat(Calculator.calculation(-2, 7, '*')).isEqualTo(-14);
        assertThat(Calculator.calculation(2, -7, '*')).isEqualTo(-14);
        assertThat(Calculator.calculation(100, 50, '/')).isEqualTo(2);
        assertThat(Calculator.calculation(-100, -50, '/')).isEqualTo(2);
        assertThat(Calculator.calculation(100, -50, '/')).isEqualTo(-2);
        assertThat(Calculator.calculation(-100, 50, '/')).isEqualTo(-2);

        // Проверка ожидаемого исключения, с использованием утверждений AssertJ:
        assertThatThrownBy(() ->
                Calculator.calculation(8, 4, '_')
        ).isInstanceOf(IllegalStateException.class);


        assertThatThrownBy(() ->
                Calculator.calculation(Integer.MAX_VALUE, 1, '+')
        ).isInstanceOf(ArithmeticException.class);

        assertThatThrownBy(() ->
                Calculator.calculation(Integer.MAX_VALUE, -1, '-')
        ).isInstanceOf(ArithmeticException.class);

        assertThatThrownBy(() ->
                Calculator.calculation(Integer.MIN_VALUE, 1, '-')
        ).isInstanceOf(ArithmeticException.class);

        assertThatThrownBy(() ->
                Calculator.calculation(Integer.MIN_VALUE, -1, '+')
        ).isInstanceOf(ArithmeticException.class);

        assertThatThrownBy(() ->
                Calculator.calculation(Integer.MAX_VALUE, 2, '*')
        ).isInstanceOf(ArithmeticException.class);

        assertThatThrownBy(() ->
                Calculator.calculation(Integer.MAX_VALUE, -2, '*')
        ).isInstanceOf(ArithmeticException.class);

        assertThatThrownBy(() ->
                Calculator.calculation(Integer.MIN_VALUE, 2, '*')
        ).isInstanceOf(ArithmeticException.class);

        assertThatThrownBy(() ->
                Calculator.calculation(Integer.MIN_VALUE, -2, '*')
        ).isInstanceOf(ArithmeticException.class);


//        System.out.println(Calculator.calculation(2_147_483_647, 1, '+')); // integer overflow
//        System.out.println(Calculator.calculation(-2_147_483_648, 1, '-')); // integer overflow


        assertThatThrownBy(() ->
                Calculator.squareRootExtraction(0)
        ).isInstanceOf(ArithmeticException.class);

        assertThatThrownBy(() ->
                Calculator.squareRootExtraction(-169)
        ).isInstanceOf(ArithmeticException.class);

//        System.out.println(Calculator.squareRootExtraction(169));

        assertThat(Calculator.calculatingDiscount(116, 5)).isEqualTo(110.2);
        assertThat(Calculator.calculatingDiscount(5641, 13)).isEqualTo(4907.67);
        assertThat(Calculator.calculatingDiscount(1248.65, 7)).isEqualTo(1161.24);
        assertThat(Calculator.calculatingDiscount(0, 7)).isEqualTo(0);
        assertThat(Calculator.calculatingDiscount(2525, 100)).isEqualTo(0);
        assertThat(Calculator.calculatingDiscount(0, 0)).isEqualTo(0);
        assertThat(Calculator.calculatingDiscount(55555555555555.55, 30))
                .isEqualTo(38888888888888.89);

        assertThatThrownBy(() ->
                Calculator.calculatingDiscount(-116, 5)
        ).isInstanceOf(ArithmeticException.class);

        assertThatThrownBy(() ->
                Calculator.calculatingDiscount(116, 105)
        ).isInstanceOf(ArithmeticException.class);

        assertThatThrownBy(() ->
                Calculator.calculatingDiscount(116, -10)
        ).isInstanceOf(ArithmeticException.class);
    }
}