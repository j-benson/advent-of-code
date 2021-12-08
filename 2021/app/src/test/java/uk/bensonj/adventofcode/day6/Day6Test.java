package uk.bensonj.adventofcode.day6;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import uk.bensonj.adventofcode.TestPuzzle;

import static org.junit.jupiter.api.Assertions.*;

class Day6Test {
    private Day6 day6;

    @BeforeEach
    void setUp() {
        day6 = new Day6(new TestPuzzle().fetchInput(6));
    }

    @Test
    void part1() {
        assertEquals(5934, day6.part1());
    }

    @Test
    void part2() {
        assertEquals(26984457539L, day6.part2());
    }
}