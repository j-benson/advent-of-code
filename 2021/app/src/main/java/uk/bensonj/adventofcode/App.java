package uk.bensonj.adventofcode;

import uk.bensonj.adventofcode.day3.Day3Part2;

public class App {
    public static void main(String[] args) {
        try {
            var input = new Puzzle().fetchInputAsLines(3);
            System.out.println(new Day3Part2().solve(input));
        } catch (Exception e) {
            System.out.printf("ERROR: %s", e);
        }
    }
}
