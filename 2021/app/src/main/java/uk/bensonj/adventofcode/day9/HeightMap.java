package uk.bensonj.adventofcode.day9;

import java.util.List;
import java.util.stream.Stream;

public class HeightMap {
    private final int width;
    private final List<Integer> heightData;

    public HeightMap(String data) {
        width = data.indexOf('\n');
        var d = data.replaceAll("\n", "");
        heightData = Stream.of(d.split("")).mapToInt(Integer::parseInt).boxed().toList();
    }

    public boolean isLow(int position) {
        return value(position) < above(position)
                && value(position) < below(position)
                && value(position) < left(position)
                && value(position) < right(position);
    }

    public int value(int position) {
        return heightData.get(position);
    }

    private int above(int position) {
        return ignoreBoundary(position - width);
    }

    private int ignoreBoundary(int p) {
        return p >= 0 && p < heightData.size() ? heightData.get(p) : Integer.MAX_VALUE;
    }

    private int below(int position) {
        return ignoreBoundary(position + width);
    }

    private int left(int position) {
        return ignoreBoundary(position - 1);
    }

    private int right(int position) {
        return ignoreBoundary(position + 1);
    }

    public int size() {
        return heightData.size();
    }
}
