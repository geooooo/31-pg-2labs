import {Point} from "./point";
import {Line} from "./line";



/*
    Экспертная система, задающая вопросы пользователю
*/
export class ExpertSystem {
    // Максимальный коэфициент сближения вершин
    private readonly _delta: number;

    public constructor(delta: number) {
        this._delta = delta;
    }

    /*
        Проверка линии на горизонтальность
    */
    public checkHorizontal(line: Line): boolean {
        let result = false;
        let absDelta = Math.abs(line.pointBegin.y - line.pointEnd.y);
        if (absDelta <= this._delta) {
            result = confirm("Выровнять линию по горизонтали ?");
        }
        return result;
    }

    /*
        Проверка линии на вертикальность
    */
    public checkVertical(line: Line): boolean {
        let result = false;
        let absDelta = Math.abs(line.pointBegin.x - line.pointEnd.x);
        if (absDelta <= this._delta) {
            result = confirm("Выровнять линию по вертикали ?");
        }
        return result;
    }

    /*
        Проверка двух линий на инцидентность
    */
    public checkIncident(line1: Line, line2: Line): string {
        let result = "";
        if (this._diffPoints(line1.pointBegin, line2.pointBegin) <= this._delta) {
            result = "bb";
        } else if (this._diffPoints(line1.pointBegin, line2.pointEnd) <= this._delta) {
            result = "be";
        } else if (this._diffPoints(line1.pointEnd, line2.pointBegin) <= this._delta) {
            result = "eb";
        } else if (this._diffPoints(line1.pointEnd, line2.pointEnd) <= this._delta) {
            result = "ee";
        }
        if ((result != "") && !confirm("Свести 2 линии в одну вершину ?")) {
            result = "";
        }
        return result;
    }

    /*
        Определение растояния между двумя точками
    */
    private _diffPoints(point1: Point, point2: Point): number {
        return Math.sqrt(Math.pow(point1.x - point2.x, 2) +
                         Math.pow(point1.y - point2.y, 2));
    }
}
