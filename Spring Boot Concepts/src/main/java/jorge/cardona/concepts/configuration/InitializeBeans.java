package jorge.cardona.concepts.configuration;

import jorge.cardona.concepts.order.Numbers;
import org.springframework.boot.ApplicationRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Profile;
import org.springframework.stereotype.Component;

import java.util.stream.Stream;

@Component
public class InitializeBeans {


    @Bean
    ApplicationRunner loadNumberOrder(Numbers positions) {
        return args -> {
            positions.printPosition();
        };
    }
}
