package seminars.first.model;

import java.util.Scanner;

public class Calculator {

    private static final Scanner scanner = new Scanner(System.in);

    public static int calculation(int firstOperand, int secondOperand, char operator) {
        int result;


        switch (operator) {
            case '+':
                result = firstOperand + secondOperand;
                if ((firstOperand > 0 && secondOperand > 0 && result < 0) ||
                        (firstOperand < 0 && secondOperand < 0 && result > 0)) {
                    throw new ArithmeticException("Integer overflow");
                }
                break;
            case '-':
                result = Calculator.calculation(firstOperand, -secondOperand, '+');
                break;
            case '*':
                if (Math.abs(secondOperand) > Integer.MAX_VALUE / Math.abs(firstOperand)) {
                    throw new ArithmeticException("Integer overflow");
                }
                result = firstOperand * secondOperand;
                break;
            case '/':
                if (secondOperand != 0) {
                    result = firstOperand / secondOperand;
                    break;
                } else {
                    throw new ArithmeticException("Division by zero is not possible");
                }
            default:
                throw new IllegalStateException("Unexpected value operator: " + operator);
        }
        return result;
    }

    public static char getOperator() {
        System.out.println("Enter operation: ");
        char operation = scanner.next().charAt(0);
        return operation;
    }

    public static int getOperand() {
        System.out.println("Enter operand: ");
        int operand;
        if (scanner.hasNextInt()) {
            operand = scanner.nextInt();
        } else {
            System.out.println("You have mistaken, try again");
            if (scanner.hasNext()) {
                scanner.next();
                operand = getOperand();
            } else {
                throw new IllegalStateException("Input error");
            }
        }
        return operand;
    }

    public static double squareRootExtraction(double number) {
        if (number == 0) {
            throw new ArithmeticException("It is not possible to extract the root from 0");
        }
        if (number < 0) {
            throw new ArithmeticException("It is impossible to extract the root from negative numbers");
        }

        double t;
        double squareRoot = number / 2;
        do {
            t = squareRoot;
            squareRoot = (t + (number / t)) / 2;
        }
        while ((t - squareRoot) != 0);
        return squareRoot;

        // или просто return Math.sqrt(number);
    }

    /**
     * @param purchaseAmount сумма покупки
     * @param discountAmount размер скидки
     * @return возвращает сумму покупки с учетом скидки
     */
    public static double calculatingDiscount(double purchaseAmount, int discountAmount) {
        if (purchaseAmount < 0) {
            throw new ArithmeticException("The amount cannot be negative");
        }
        if (discountAmount < 0 || discountAmount > 100) {
            throw new ArithmeticException("The discount should be from 0 to 100%");
        }
        return Math.round((100 - discountAmount) * purchaseAmount) / 100.0;
    }
}