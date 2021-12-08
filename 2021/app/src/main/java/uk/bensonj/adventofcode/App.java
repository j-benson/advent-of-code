package uk.bensonj.adventofcode;

import uk.bensonj.adventofcode.day6.Day6;

public class App {
    public static void main(String[] args) {
        try {
            var puzzle = new Puzzle();
            var answer = new Day6(puzzle.fetchInput(6)).part2();
            System.out.println(answer);
            //System.out.println(puzzle.submit(6, 1, answer));
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
