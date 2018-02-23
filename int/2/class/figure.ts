import {Point} from "./point";
import {Line} from "./line";



/*
    Фигура, представленая последовательностью точек вершин
*/
export class Figure {
    // Вершины фигуры
    private _points: Point[];
    // Цвет контура фигуры
    private _lineColor: string;
    // Толщина контура фигуры
    private _lineWidth: number;

    /*
        Создание фигуры по заданым вершинам, цвету и толщине контура
    */
    public constructor(points: Point[], lineColor: string, lineWidth: number) {
        this._points = points;
        this._lineColor = lineColor;
        this._lineWidth = lineWidth;
    }

    public get points(): Point[] {
        return this._points;
    }

    public lines(): Line[] {
        let result: Line[] = [];
        let inc = 2;
        if (this._points.length > 2) {
            inc = 1;
        }
        for (let i = 0; i < this._points.length-1; i += inc) {
            result.push(new Line(this._points[i], this._points[i+1]));
        }
        return result;
    }

    public get lineWidth(): number {
        return this._lineWidth;
    }

    public get lineColor(): string {
        return this._lineColor;
    }

    public set lineColor(value: string) {
        this._lineColor = value;
    }

}
