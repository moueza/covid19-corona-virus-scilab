package main;

import org.springframework.beans.factory.annotation.Autowired;

import services.BookingService;
import services.TransferServiceI;
import services.TransferServiceImpl;

public class Main {

	/**
	 * https://stackoverflow.com/questions/48883984/alternative-to-applicationcontext-getbean-in-spring
	 */
	@Autowired
	TransferServiceI transferService;

	@Autowired
	BookingService bookingService;

	public static void main(String[] args) {
		Main main = new Main();
	//	System.out.println("last=" + main.bookingService.book("Alice", "Bob", "Carol"));

		System.out.println("id=" + main.transferService.id2daorequest());

	}
}
