(define a '(lambda (a b) (+ a b)))
(define (caar x) (car (car x)))

(define (cadr x) (car (cdr x)))

(define (cdar x) (cdr (car x)))

(define (cddr x) (cdr (cdr x)))
(define form (car a))
form
(define param (cadr a))
param
(define body (cddr a))
body
((lambda (a b) (+ a b)) 1 2)
