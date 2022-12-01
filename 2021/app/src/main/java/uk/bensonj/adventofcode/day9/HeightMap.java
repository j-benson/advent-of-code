package uk.bensonj.adventofcode.day9;

import java.util.ArrayList;
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
        return value(position) < valueAbove(position)
                && value(position) < valueBelow(position)
                && value(position) < valueLeft(position)
                && value(position) < valueRight(position);
    }

    public int discoverBasinSizeFromLowPoint(int lowPosition) {
        return higherGround(lowPosition);
    }
    private int higherGround(int position) {
        if (value(position) == 9) {
            return 0;
        }
        var highGround = new ArrayList<Integer>();
        if (valueAbove(position) > value(position)) {
            highGround.add(positionAbove(position));
        }
        if (valueBelow(position) > value(position)) {
            highGround.add(positionBelow(position));
        }
        if (valueLeft(position) > value(position)) {
            highGround.add(positionLeft(position));
        }
        if (valueRight(position) > value(position)) {
            highGround.add(positionRight(position));
        }
        return highGround.stream().mapToInt(this::higherGround).sum() + 1;
    }

    public int value(int position) {
        return valueBoundaryWall(position);
    }

    private int valueAbove(int position) {
        return valueBoundaryWall(positionAbove(position));
    }

    private int valueBoundaryWall(int p) {
        return p >= 0 && p < p % width && p < heightData.size() ? heightData.get(p) : 9;
    }

    private int positionAbove(int position) {
        return position - width;
    }

    private int valueBelow(int position) {
        return valueBoundaryWall(positionBelow(position));
    }

    private int positionBelow(int position) {
        return position + width;
    }

    private int valueLeft(int position) {
        return valueBoundaryWall(positionLeft(position));
    }

    private int positionLeft(int position) {
        return position - 1;
    }

    private int valueRight(int position) {
        return valueBoundaryWall(positionRight(position));
    }

    private int positionRight(int position) {
        return position + 1;
    }

    public int size() {
        return heightData.size();
    }
}
