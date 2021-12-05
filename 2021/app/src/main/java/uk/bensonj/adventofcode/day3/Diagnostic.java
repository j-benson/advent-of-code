package uk.bensonj.adventofcode.day3;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.atomic.AtomicReference;
import java.util.function.Function;
import java.util.stream.IntStream;

public class Diagnostic {
    private final int wordSize;
    private final String highBitMask, lowBitMask;
    private final List<String> report;

    public Diagnostic(List<String> report) {
        this.report = report;
        wordSize = report.get(0).length();
        highBitMask = highBitMask(report);
        lowBitMask = lowBitMask(highBitMask);
    }

    public int gammaRate() {
        return Integer.parseUnsignedInt(highBitMask, 2);
    }

    public int epsilonRate() {
        return Integer.parseUnsignedInt(lowBitMask, 2);
    }

    public int oxygenGeneratorRating() {
        return applyMask(highBitMask, this::highBitMask);
    }

    public int co2ScrubberRating() {
        return applyMask(lowBitMask, (words) -> lowBitMask(highBitMask(words)));
    }

    private int applyMask(String startingMask, Function<List<String>, String> maskFunction) {
        var copy = new ArrayList<>(report);
        var mask = new AtomicReference<>(startingMask);
        var rating = new AtomicInteger();
        IntStream.range(0, highBitMask.length()).takeWhile(i -> copy.size() > 1).forEach(i -> {
            if (copy.removeIf(word -> !word.split("")[i].equals(mask.get().split("")[i]))) {
                mask.set(maskFunction.apply(copy));
            }
            if (copy.size() == 1) {
                rating.set(Integer.parseUnsignedInt(copy.get(0), 2));
            }
        });
        return rating.get();
    }

    private String highBitMask(List<String> input) {
        StringBuilder mask = new StringBuilder();
        IntStream.range(0, input.get(0).length()).forEach(i -> {
            var columnBitSum = input.stream().mapToInt(n -> Integer.parseInt(n.split("")[i])).sum();
            var isHigh = columnBitSum >= input.size() / 2.0;
            mask.append(isHigh ? "1" : "0");
        });
        return mask.toString();
    }

    private String lowBitMask(String highBitMask) {
        var highBitMaskValue = Integer.parseUnsignedInt(highBitMask, 2);
        var lowBitMaskValue = switch (wordSize) {
            case 5 -> highBitMaskValue ^ 0B11111;
            case 12 -> highBitMaskValue ^ 0B111111111111;
            default -> throw new IllegalArgumentException();
        };
        var lowBitMaskBinary = new StringBuilder(Integer.toString(lowBitMaskValue, 2));
        while (lowBitMaskBinary.length() < wordSize) {
            lowBitMaskBinary.insert(0, "0");
        }
        return lowBitMaskBinary.toString();
    }
}
