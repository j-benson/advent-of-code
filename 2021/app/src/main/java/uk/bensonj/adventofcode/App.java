package uk.bensonj.adventofcode;

import uk.bensonj.adventofcode.day1.Part2;

public class App {
    public static void main(String[] args) {
        try {
            var input = new Utils().fetchPuzzleInputAsLines(1);
            System.out.println(new Part2().solve(input));
        } catch (Exception e) {
            System.out.printf("ERROR: %s", e);
        }
    }
}
