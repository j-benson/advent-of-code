package uk.bensonj.adventofcode.day1;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.*;

class Part2Test {
    private Part2 part2;

    @BeforeEach
    public void setUp() {
        part2 = new Part2();
    }

    @Test
    void solve() {
        var result = part2.solve(Arrays.asList(
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

        assertEquals(5, result);
    }

}