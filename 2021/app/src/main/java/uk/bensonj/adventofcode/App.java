package uk.bensonj.adventofcode;

import uk.bensonj.adventofcode.day2.Day2Part2;

public class App {
    public static void main(String[] args) {
        try {
            var input = new Puzzle().fetchInputAsLines(2);
            System.out.println(new Day2Part2().solve(input));
        } catch (Exception e) {
            System.out.printf("ERROR: %s", e);
        }
    }
}
