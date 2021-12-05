package uk.bensonj.adventofcode.day4;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import uk.bensonj.adventofcode.TestPuzzle;

import static org.junit.jupiter.api.Assertions.*;

class Day4Test {
    private TestPuzzle testPuzzle;
    private Day4 day4;

    @BeforeEach
    void setUp() {
        testPuzzle = new TestPuzzle();
        day4 = new Day4();
    }

    @Test
    void part1() {
        assertEquals(4512, day4.part1(testPuzzle.fetchInput(4)));
    }

    @Test
    void part2() {
        assertEquals(1924, day4.part2(testPuzzle.fetchInput(4)));
    }
}