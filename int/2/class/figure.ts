import {Point} from "./point";



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
