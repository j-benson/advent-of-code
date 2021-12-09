package uk.bensonj.adventofcode.day7;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import uk.bensonj.adventofcode.TestPuzzle;

import static org.junit.jupiter.api.Assertions.*;

class Day7Test {
    private Day7 day7;

    @BeforeEach
    void setUp() {
        day7 = new Day7(new TestPuzzle().fetchInput(7));
    }

    @Test
    void part1() {
        assertEquals(37, day7.part1());
    }

    @Test
    void part2() {
        assertEquals(0, day7.part2());
    }
}