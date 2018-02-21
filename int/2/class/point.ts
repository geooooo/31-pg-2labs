/*
    Точка на плоскости
*/
export class Point {
    // Координаты точки
    private _x: number;
    private _y: number;

    public constructor(x: number, y: number) {
        this._x = x;
        this._y = y;
    }

    public get x(): number {
        return this._x;
    }

    public get y(): number {
        return this._y;
    }

    /*
        Сравнение с другой точкой
    */
    public equal(point: Point): boolean {
        return (this._x == point.x) && (this._y == point.y);
    }
}
