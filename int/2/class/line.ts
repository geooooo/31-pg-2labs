import {Point} from "./point";



/*
    Отрезок на плоскости
*/
export class Line {
    // Координаты концов отрезка
    private _pointBegin: Point;
    private _pointEnd: Point;

    public constructor(pointBegin: Point, pointEnd: Point) {
        this._pointBegin = pointBegin;
        this._pointEnd = pointEnd;
    }

    public get pointBegin(): Point {
        return this._pointBegin;
    }

    public get pointEnd(): Point {
        return this._pointEnd;
    }
}
