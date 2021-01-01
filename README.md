# morm
Alternative to the fitting module of f. Transforms axes until they are linear instead of trying to define a function


This uses xevo (my package) and randomly transforms either x or y to maximize linearity (where I define linearity as the correlation between the x and the y axis)(thinking about this abs(correlation) would be more general, without it it generates growing functions)

This works much easier, since linearity is much more continuos than the l2 loss of f, but it has a huge drawback by not beeing able to mutate multiparameter functions (like the + in x+sin(x)). This is because I dont want to guess values. That beeing said, additions can still be solved by the combination of two existing linearities (sin(x)^2+x gets more linear through combining (averaging) it with cos(x)^2)

What made this interresting for me, is that the whole analysis is databased: When x is big, sinh(x)=exp(x)/2 and asinh(x)+exp(asinh(x))=linear
