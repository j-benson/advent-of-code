package uk.bensonj.adventofcode.day5;

import uk.bensonj.adventofcode.NopeException;

import java.util.HashMap;
import java.util.List;
import java.util.Objects;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.IntStream;

public class Hydrothermal {
    private List<Line> lines;

    public Hydrothermal(List<String> input) {
        lines = input.stream().map(Line::new).toList();
    }

    public void excludeDiagonals() {
        lines = lines.stream().filter(line -> line.a.x == line.b.x || line.a.y == line.b.y).toList();
    }
    public int dangerZones() {
        var pointMap = new HashMap<Point, Integer>(lines.size() * 10);
        lines.stream().map(Line::pointsOnLine)
                .flatMap(List::stream)
                .forEach(p -> {
                    int count = pointMap.getOrDefault(p, 0);
                    pointMap.put(p, count + 1);
                });
        return pointMap.values().stream().filter(i -> i > 1).toList().size();
    }
}

class Line {
    final Point a, b;

    public Line(String data) {
        var points = data.split(" -> ");
        a = new Point(points[0]);
        b = new Point(points[1]);
    }
    public List<Point> pointsOnLine() {
        if (a.x == b.x) {
            return numbersBetweenInclusive(a.y, b.y).mapToObj(i -> new Point(a.x, i)).toList();
        } else if (a.y == b.y) {
            return numbersBetweenInclusive(a.x, b.x).mapToObj(i -> new Point(i, a.y)).toList();
        } else {
            var lowXPoint = Math.min(a.x, b.x) == a.x ? a : b;
            var highXPoint = lowXPoint == a ? b : a;
            var direction = lowXPoint.y < highXPoint.y ? 1 : -1;
            var y = new AtomicInteger(lowXPoint.y);
            return numbersBetweenInclusive(lowXPoint.x, highXPoint.x)
                    .mapToObj(x -> new Point(x, y.getAndUpdate(i -> i + direction))).toList();
        }
    }
    private IntStream numbersBetweenInclusive(int a, int b) {
        return IntStream.rangeClosed(Math.min(a, b), Math.max(a, b));
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Line line = (Line) o;
        return Objects.equals(a, line.a) && Objects.equals(b, line.b);
    }
    @Override
    public int hashCode() {
        return Objects.hash(a, b);
    }
    @Override
    public String toString() {
        return "%s -> %s".formatted(a, b);
    }
}

class Point {
    final int x, y;

    public Point(String data) {
        var points = data.split(",");
        x = Integer.parseInt(points[0]);
        y = Integer.parseInt(points[1]);
    }
    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Point point = (Point) o;
        return x == point.x && y == point.y;
    }
    @Override
    public int hashCode() {
        return Objects.hash(x, y);
    }
    @Override
    public String toString() {
        return "%d,%d".formatted(x, y);
    }
}
