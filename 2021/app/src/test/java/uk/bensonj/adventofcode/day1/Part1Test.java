package uk.bensonj.adventofcode.day1;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.*;

class Part1Test {
    private Part1 part1;

    @BeforeEach
    public void setUp() {
        part1 = new Part1();
    }

    @Test
    void solve() {
        var result = part1.solve(Arrays.asList(
                "199",
                "200",
                "208",
                "210",
                "200",
                "207",
                "240",
                "269",
                "260",
                "263"
        ));

        assertEquals(7, result);
    }
}
