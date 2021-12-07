package uk.bensonj.adventofcode.day5;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import uk.bensonj.adventofcode.TestPuzzle;

import static org.junit.jupiter.api.Assertions.*;

class Day5Test {
    private Day5 day5;

    @BeforeEach public void setUp() {
        day5 = new Day5(new TestPuzzle().fetchInputAsLines(5));
    }

    @Test public void part1() {
        assertEquals(5, day5.part1());
    }

    @Test public void part2() {
        assertEquals(12, day5.part2());
    }
}
