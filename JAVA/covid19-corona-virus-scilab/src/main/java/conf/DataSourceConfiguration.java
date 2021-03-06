package conf;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import entities.Bar;
import entities.Foo;
import services.TransferServiceImpl;
import services.BookingService;
import services.TransferServiceI;
import conf.*;

/**
 * https://docs.spring.io/spring-javaconfig/docs/1.0.0.m3/reference/html/creating-bean-definitions.html
 * 
 * https://docs.spring.io/spring-framework/docs/4.2.x/spring-framework-reference/html/
 */
//@Configuration(defaultAutowire = Autowire.BY_TYPE, defaultLazy = Lazy.FALSE)
@Configuration()
public class DataSourceConfiguration {
	// bean definitions follow
	/**
	 * PDF
	 * https://docs.spring.io/spring-javaconfig/docs/1.0.0.M4/reference/pdf/spring-javaconfig-reference.pdf
	 * 
	 * 4.2.4
	 * https://docs.spring.io/spring-javaconfig/docs/1.0.0.m3/reference/html/creating-bean-definitions.html
	 * Singleton scope as default
	 */
	@Bean
	public TransferServiceI transferService() {
		return new TransferServiceImpl();
	}

	/**
	 * PDF
	 * https://docs.spring.io/spring-javaconfig/docs/1.0.0.M4/reference/pdf/spring-javaconfig-reference.pdf
	 */
	@Bean
	public Foo foo() {
		return new Foo(bar());
	}

	@Bean
	public Bar bar() {
		return new Bar();
	}

	/**
	 * https://stackoverflow.com/questions/34172888/difference-between-bean-and-autowired
	 */
	@Bean
	BookingService bookingService() {
		return new BookingService();
	}
}
