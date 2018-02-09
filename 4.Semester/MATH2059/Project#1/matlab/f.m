function result = f(x)

    result = 3 * sin((x .^ (3 .* x)) ./ x) .* tan(log(3 .* exp(0.2 .* sin(x)) .* x))

end