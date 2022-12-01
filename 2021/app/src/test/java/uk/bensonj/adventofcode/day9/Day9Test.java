package uk.bensonj.adventofcode.day9;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import uk.bensonj.adventofcode.TestPuzzle;

import static org.junit.jupiter.api.Assertions.*;

class Day9Test {
    private Day9 day9;

    @BeforeEach
    void setUp() {
        day9 = new Day9(new TestPuzzle().fetchInput(9));
    }

    @Test
    void part1() {
        assertEquals(15, day9.part1());
    }

    @Test
    void part2() {
        assertEquals(1134, day9.part2());
    }
}