import {Point} from "./point";
import {Line} from "./line";
import {Figure} from "./figure";
import {ExpertSystem} from "./expertsystem";



/*
    Класс-синглтон для доступа к полотну
*/
export class Canvas {
    // Цвет заливки при очистке полотна
    private readonly _CLEAR_COLOR = "#ddd";
    // Цвет линии
    private readonly _LINE_DEFAULT_COLOR = "#417ba8";
    // Цвет выбранной линии
    private readonly _LINE_SELECT_COLOR = "#6a41a8";
    // Ширина линии
    private readonly _LINE_WIDTH = 8;

    // Синглтон текущего класса
    private static _instance: Canvas = null;
    // HTML-элемент полотна
    private _canvas: any;
    // HTML-элемент блока для вывода координат курсора
    private _xy: HTMLElement;
    // Контекст рисования
    private _context2D: CanvasRenderingContext2D;
    // Список фигур на полотне
    private _figures: Figure[] = [];
    // Список выбранных фигур
    private _selectedFigures: Figure[] = [];
    // Экспертная подсистема
    private _expertSystem = new ExpertSystem(30);

    /*
        Привязка синглтона к полотну и получение контекса для рисования
    */
    public constructor() {
        if (Canvas._instance == null) {
            this._canvas = document.getElementById("canvas");
            this._context2D = this._canvas.getContext("2d");
            this._xy = document.getElementById("xy");
            Canvas._instance = this;
            this._eventBinding();
            this._clear();
        }
        return Canvas._instance;
    }

    /*
        Проверка принадлежности точки к отрезку
    */
    private _lineHasPoint(lineBegin: Point, lineEnd: Point, point: Point): boolean {
        let x = point.x;
        let y = point.y;
        // Массив X-координат полигона
        let xp = [
            lineBegin.x - Math.floor(this._LINE_WIDTH / 2),
            lineBegin.x + Math.floor(this._LINE_WIDTH / 2),
            lineEnd.x + Math.floor(this._LINE_WIDTH / 2),
            lineEnd.x - Math.floor(this._LINE_WIDTH / 2)
        ];
        // Массив Y-координат полигона
        let yp = [
            lineBegin.y - Math.floor(this._LINE_WIDTH / 2),
            lineBegin.y + Math.floor(this._LINE_WIDTH / 2),
            lineEnd.y + Math.floor(this._LINE_WIDTH / 2),
            lineEnd.y - Math.floor(this._LINE_WIDTH / 2)
        ];
        var npol = xp.length;
        let j = npol - 1;
        let c = false;
        for (let i = 0; i < npol; i++) {
            if ((((yp[i] <= y) && (y < yp[j])) || ((yp[j] <= y) && (y < yp[i]))) &&
                (x > (xp[j] - xp[i]) * (y - yp[i]) / (yp[j] - yp[i]) + xp[i]))
            {
                c = !c
            }
            j = i;
        }
        return c;
    }

    /*
        Поиск фигуры, которой принадлежит точка
    */
    private _getFigureHasPoint(point: Point): Figure {
        let result: Figure = null;
        console.log(this._figures);
    outer:
        for (let figure of this._figures) {
            console.log(figure.points);
            if (figure.points.length > 2) {
                for (let i = 0; i < figure.points.length-1; i++) {
                    let lineBegin = new Point(figure.points[i].x, figure.points[i].y);
                    let lineEnd = new Point(figure.points[i+1].x, figure.points[i+1].y);
                    if (this._lineHasPoint(lineBegin, lineEnd, point)) {
                        result = figure;
                        break outer;
                    }
                }
            } else {
                let lineBegin = new Point(figure.points[0].x, figure.points[0].y);
                let lineEnd = new Point(figure.points[1].x, figure.points[1].y);
                if (this._lineHasPoint(lineBegin, lineEnd, point)) {
                    result = figure;
                    break outer;
                }
            }

        }
        return result;
    }

    /*
        Отрисовка фигуры на полотне
    */
    private _draw(figure: Figure): void {
        this._context2D.beginPath();
        this._context2D.strokeStyle = figure.lineColor;
        this._context2D.lineWidth = figure.lineWidth;
        this._context2D.lineCap = "round";
        this._context2D.lineJoin = "round";
        this._context2D.moveTo(figure.points[0].x, figure.points[0].y);
        for (let point of figure.points.slice(1, figure.points.length)) {
            this._context2D.lineTo(point.x, point.y);
        }
        this._context2D.stroke();
    }

    /*
        Очистка полотна
    */
    private _clear(): void {
        this._context2D.fillStyle = this._CLEAR_COLOR;
        this._context2D.fillRect(
            0, 0,
            Number(this._canvas.clientHeight),
            Number(this._canvas.clientWidth)
        );
    }

    /*
        Отрисовка всех фигур
    */
    private _drawAll(): void {
        this._clear();
        for (let figure of this._figures) {
            this._draw(figure);
        }
    }

    /*
        Пометка фигуры как выбранной/не выбранной
    */
    private _toggleSelect(figure: Figure): void {
        if (figure.lineColor == this._LINE_DEFAULT_COLOR) {
            figure.lineColor = this._LINE_SELECT_COLOR;
            this._selectedFigures.push(figure);
        } else {
            figure.lineColor = this._LINE_DEFAULT_COLOR;
            this._selectedFigures = this._selectedFigures.filter((figure0) => {
                return figure != figure0;
            });
        }
        this._drawAll();
    }

    /*
        Удаление выделеных фигур
    */
    private _deleteSelected(): void {
        this._figures = this._figures.filter((figure0) => {
            for (let selectedFigure of this._selectedFigures) {
                if (selectedFigure == figure0) {
                    return false;
                }
            }
            return true;
        });
        this._selectedFigures = [];
        this._drawAll();
    }

    /*
        Снятие выделения со всех фигур
    */
    private _clearSelection(): void {
        for (let figure of this._selectedFigures) {
            this._toggleSelect(figure);
        }
        this._selectedFigures = [];
    }

    /*
        Назначение обработчиков событий
    */
    private _eventBinding(): void {
        let firstPoint: Point = null;
        this._canvas.addEventListener("mousemove", (e) => {
            // Вывод координат курсора
            this._xy.innerHTML = `${e.layerX} : ${e.layerY}`;
            // Растяжение линии
            if (firstPoint != null) {
                let secondPoint = new Point(e.layerX, e.layerY);
                let figure = new Figure(
                    [firstPoint, secondPoint],
                    this._LINE_DEFAULT_COLOR,
                    this._LINE_WIDTH
                )
                this._drawAll();
                this._draw(figure);
            }
        });
        this._canvas.addEventListener("mouseleave", (e) => {
            this._xy.innerHTML = "";
        });
        this._canvas.addEventListener("click", (e) => {
            if (firstPoint == null) {
                let point = new Point(e.layerX, e.layerY);
                if (e.ctrlKey) {
                    // Выделить/снять выделение фигуры
                    let figure = this._getFigureHasPoint(point);
                    if (figure == null) {
                        return;
                    }
                    this._toggleSelect(figure);
                    // Проверка на инцидентность
                    if (this._selectedFigures.length == 2) {
                        let figureLines1 = this._selectedFigures[0].lines();
                        let line1: Line;
                        if (figureLines1.length > 1) {
                            line1 = new Line(figureLines1[0].pointBegin,
                                             figureLines1[figureLines1.length-1].pointEnd);
                        } else {
                            line1 = figureLines1[0];
                        }
                        let figureLines2 = this._selectedFigures[1].lines();
                        let line2: Line;
                        if (figureLines2.length > 1) {
                            line2 = new Line(figureLines2[0].pointBegin,
                                             figureLines2[figureLines2.length-1].pointEnd);
                        } else {
                            line2 = figureLines2[0];
                        }
                        console.log(figureLines1, figureLines2);
                        let result = this._expertSystem.checkIncident(line1, line2);
                        let figure1 = this._selectedFigures[0]
                        let figure2 = this._selectedFigures[1]
                        let newFigurePoints: Point[] = [];
                        switch (result) {
                            case "bb":
                                for (let i = figure1.points.length-1; i >= 0; i--) {
                                    newFigurePoints.push(figure1.points[i]);
                                }
                                for (let i = 1; i < figure2.points.length; i++) {
                                    newFigurePoints.push(figure2.points[i]);
                                }
                                break;
                            case "eb":
                                for (let i = 0; i < figure1.points.length; i++) {
                                    newFigurePoints.push(figure1.points[i]);
                                }
                                for (let i = 1; i < figure2.points.length; i++) {
                                    newFigurePoints.push(figure2.points[i]);
                                }
                                break;
                            case "be":
                                for (let i = figure1.points.length-1; i >= 0; i--) {
                                    newFigurePoints.push(figure1.points[i]);
                                }
                                for (let i = figure2.points.length-2; i >= 0; i--) {
                                    newFigurePoints.push(figure2.points[i]);
                                }
                                break;
                            case "ee":
                                for (let i = 0; i < figure1.points.length; i++) {
                                    newFigurePoints.push(figure1.points[i]);
                                }
                                for (let i = figure2.points.length-2; i >= 0; i--) {
                                    newFigurePoints.push(figure2.points[i]);
                                }
                                break;
                            default:
                                return;
                        }
                        this._figures.push(new Figure(
                            newFigurePoints,
                            this._LINE_DEFAULT_COLOR,
                            figure1.lineWidth
                        ));
                        this._deleteSelected();
                        this._drawAll();
                    }
                } else {
                    // Начать растяжение линии
                    this._clearSelection();
                    firstPoint = point;
                }
            } else {
                // Отрисовка линии и добавление в список
                let secondPoint = new Point(e.layerX, e.layerY);
                let secondX = e.layerX;
                let secondY = e.layerY;
                if (this._expertSystem.checkVertical(new Line(firstPoint, secondPoint))) {
                    secondX = firstPoint.x;
                } else if (this._expertSystem.checkHorizontal(new Line(firstPoint, secondPoint))) {
                    secondY = firstPoint.y;
                }
                secondPoint = new Point(secondX, secondY);
                let figure = new Figure(
                    [firstPoint, secondPoint],
                    this._LINE_DEFAULT_COLOR,
                    this._LINE_WIDTH
                )
                this._figures.push(figure);
                this._drawAll();
                firstPoint = null;
            }
        });
        window.addEventListener("keypress", (e) => {
            switch (e.key.toLowerCase()) {
                case "c":
                    // Снятие выделений
                    this._clearSelection();
                    break;
                case "d":
                    // Удаление выделеных фигур
                    this._deleteSelected();
                    break;
                case "t":
                    // Отладочные данные в консоль
                    console.clear();
                    console.log("Figures:");
                    console.log(this._figures);
                    console.log("Selected figures:");
                    console.log(this._selectedFigures);
                    break;
            }
        });
    }

}
