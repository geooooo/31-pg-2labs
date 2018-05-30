(deftemplate line
  (slot id (type INTEGER)(default 0))
  (slot x1 (type INTEGER)(default 0))
  (slot y1 (type INTEGER)(default 0))
  (slot x2 (type INTEGER)(default 0))
  (slot y2 (type INTEGER)(default 0))
)

(deffacts lines
  (line (id 1) (x1 14) (y1 4 ) (x2 53) (y2 35))
  (line (id 2) (x1 52) (y1 10) (x2 61) (y2 21))
  (line (id 3) (x1 31) (y1 15) (x2 25) (y2  4))
  (line (id 4) (x1 75) (y1 75) (x2  0) (y2  0))
  (line (id 5) (x1  7) (y1 15) (x2 15) (y2  7))
  (line (id 6) (x1 12) (y1 44) (x2 31) (y2 53))
  (line (id 7) (x1 26) (y1 21) (x2 54) (y2 14))
  (line (id 8) (x1 94) (y1 32) (x2 52) (y2 68))
  (line (id 9) (x1 98) (y1 87) (x2 78) (y2 93))
  (line (id 10) (x1 5) (y1 5) (x2 15) (y2 6))
  (line (id 11) (x1 5) (y1 5) (x2 5) (y2 15))
)

(deffunction checkConst (?x)
  (< (abs ?x) 3)
)
(deffunction sqr (?x)
  (* ?x ?x)
)
(deffunction dist (?x1 ?y1 ?x2 ?y2)
 (sqrt
	(+
		(sqr (- ?x2 ?x1))
		(sqr (- ?y2 ?y1))
	)
  )
)

(defrule isVertical
  (line (id ?lid) (x1 ?lx1) (y1 ?ly1) (x2 ?lx2) (y2 ?ly2))
  (test (checkConst (- ?lx2 ?lx1)))
  =>
  (printout t "Line #" ?lid " is vertical" crlf)
)

(isVertical? 1)

(defrule isHorizontal
  (line (id ?lid) (x1 ?lx1) (y1 ?ly1) (x2 ?lx2) (y2 ?ly2))
  (test(checkConst (- ?ly2 ?ly1)))
  =>
  (printout t "Line #" ?lid " is horizontal" crlf)
)

(defrule isClose
	(line (id ?l1id) (x1 ?l1x1) (y1 ?l1y1) (x2 ?l1x2) (y2 ?l1y2))
	(line (id ?l2id) (x1 ?l2x1) (y1 ?l2y1) (x2 ?l2x2) (y2 ?l2y2))

	(test
	  (and
	    (< ?l1id ?l2id)
	    (or
	      (checkConst (dist ?l1x1 ?l1y1 ?l2x1 ?l2y1))
     	  (checkConst (dist ?l1x1 ?l1y1 ?l2x2 ?l2y2))
	      (checkConst (dist ?l1x2 ?l1y2 ?l2x1 ?l2y1))
	      (checkConst (dist ?l1x2 ?l1y2 ?l2x2 ?l2y2))
	    )
	  )
	)
	=>
	(printout t "Lines #" ?l1id " and #" ?l2id " are close" crlf)
)

(defrule isScaled11
	(line (id ?l1id) (x1 ?l1x1) (y1 ?l1y1) (x2 ?l1x2) (y2 ?l1y2))
	(line (id ?l2id) (x1 ?l2x1) (y1 ?l2y1) (x2 ?l2x2) (y2 ?l2y2))
	(test(< ?l1id ?l2id))
	(test
		(checkConst
			(-
				(dist ?l1x1 ?l1y1 ?l1x2 ?l1y2)
				(dist ?l2x1 ?l2y1 ?l2x2 ?l2y2)
			)
		)
	)
=>
	(printout t "Line #" ?l1id " scaled to line #" ?l2id " like 1:1" crlf)
)
(defrule isScaled21
	(line (id ?l1id) (x1 ?l1x1) (y1 ?l1y1) (x2 ?l1x2) (y2 ?l1y2))
	(line (id ?l2id) (x1 ?l2x1) (y1 ?l2y1) (x2 ?l2x2) (y2 ?l2y2))
	(test(<> ?l1id ?l2id))
	(test
		(checkConst
			(-
				(* 2 (dist ?l1x1 ?l1y1 ?l1x2 ?l1y2))
				(dist ?l2x1 ?l2y1 ?l2x2 ?l2y2)
			)
		)
	)
=>
	(printout t "Line #" ?l1id " scaled to line #" ?l2id " like 2:1" crlf)
)

(defrule isScaled31
	(line (id ?l1id) (x1 ?l1x1) (y1 ?l1y1) (x2 ?l1x2) (y2 ?l1y2))
	(line (id ?l2id) (x1 ?l2x1) (y1 ?l2y1) (x2 ?l2x2) (y2 ?l2y2))
	(test(<> ?l1id ?l2id))
	(test
		(checkConst
			(-
				(* 3 (dist ?l1x1 ?l1y1 ?l1x2 ?l1y2))
				(dist ?l2x1 ?l2y1 ?l2x2 ?l2y2)
			)
		)
	)
=>
	(printout t "Line #" ?l1id " scaled to line #" ?l2id " like 3:1" crlf)
)
