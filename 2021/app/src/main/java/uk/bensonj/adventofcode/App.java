package uk.bensonj.adventofcode;

import uk.bensonj.adventofcode.day4.Day4;

public class App {
    public static void main(String[] args) {
        try {
            System.out.println(new Day4().part2(new Puzzle().fetchInput(4)));
        } catch (Exception e) {
            System.out.printf("ERROR: %s", e);
        }
    }
}
