using SymPy

@vars x 
γ = symbols("γ", real=true, positive=true)
σ = symbols("σ", real=true, positive=true)


function lorentz(x, γ)
    # non-normnormalized Lorentzian
    return 1/(γ^2 + x^2)
end


function gauss(x, σ)
    # non-normalized Gaussian
   return exp(-x^2/2σ^2)
end


println("Finding the norm of Lorentzian:")
lorentz_integral = sympy.Integral(lorentz(x,γ), (x, -oo, oo))
lorentz_norm = lorentz_integral.doit()
println(lorentz_integral, " = ", lorentz_norm)
#println(Eq(lorentz_integral, lorents_norm ))
println()

println("Calculating the half width at half maximum (hwhm) of Lorenzian:")
lorentz_max = lorentz(0, γ)
lorentz_hwhm = Eq(lorentz(x, γ), 1//2*lorentz_max)
println(lorentz_hwhm)
x_half_max_lorentz = solve(lorentz_hwhm, x)
println("x at half max = ", x_half_max_lorentz)
println()

##############################################################################

println("Finding the norm of Gaussian:")
gauss_integral = sympy.Integral(gauss(x,σ), (x, -oo, oo))
gauss_norm = gauss_integral.doit()
println(gauss_integral, " = ", gauss_norm)
#println(Eq(gauss_integral, gauss_norm))
println()

println("Calculating the half width at half maximum (hwhm) of Gaussian:")
gauss_max = gauss(0, σ)
gauss_hwhm = Eq(gauss(x, σ), (1//2)*gauss_max)
println(gauss_hwhm)
solve(gauss_hwhm, x)
x_half_max_gauss = solve(gauss_hwhm, x)
println("x at half max = ", x_half_max_gauss)

# example: generating LaTeX code for the displayed equations:
# print(latex(Eq(L_int, L_norm )))