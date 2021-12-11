package uk.bensonj.adventofcode.modules;

import java.util.stream.IntStream;

public class MathUtils {
    public static int triangular(int value) {
        return IntStream.rangeClosed(1, value).sum();
    }
}
