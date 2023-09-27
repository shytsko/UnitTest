package seminars.first.hw;

import java.util.Arrays;
import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;

public class ShopTest {

    public static void main(String[] args) {
        Product p1 = new Product("product1", 33);
        Product p2 = new Product("product2", 22);
        Product p3 = new Product("product3", 55);
        Product p4 = new Product("product4", 44);
        Product p5 = new Product("product5", 11);

        Shop shop = new Shop(Arrays.asList(p1, p2, p3, p4, p5));
        System.out.println(shop.getProducts());

// 1. Проверить, что магазин хранит верный список продуктов (количество продуктов, состав корзины)

        assertThat(shop.getProducts())
                .hasSize(5)
                .contains(p1, p2, p3, p4, p5);

// 2. Проверить, что магазин возвращает верный самый дорого продукт getMostExpensiveProduct
        assertThat(shop.getMostExpensiveProduct()).isEqualTo(p3);

// 3. Проверить, что магазин возвращает верный отсортированный по цене список продуктов
        List<Product> products_sorted = shop.getSortedListProducts();
        System.out.println(products_sorted);
        assertThat(products_sorted)
                .hasSize(5)
                .containsSequence(p5, p2, p1, p4, p3);
    }
}




