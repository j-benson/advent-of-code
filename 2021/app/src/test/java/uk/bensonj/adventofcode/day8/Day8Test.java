package uk.bensonj.adventofcode.day8;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import uk.bensonj.adventofcode.TestPuzzle;

import static org.junit.jupiter.api.Assertions.*;

class Day8Test {
    private Day8 day8;

    @BeforeEach
    public void setUp() {
        day8 = new Day8(new TestPuzzle().fetchInputAsLines(8));
    }

    @Test
    void part1() {
        assertEquals(26, day8.part1());
    }

    @Test
    void part2() {
        assertEquals(0, day8.part2());
    }
}