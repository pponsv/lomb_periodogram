close 'all'

t = linspace(0, 2, 2001);

modes = makemodes(3, 500, 10);
disp(modes)

ncoils=15;
phis = 2*pi*rand(ncoils,1);
thetas = 2*pi*rand(ncoils,  1);

sig = makesig(t, phis, thetas, modes);

f = modes(1,2);
[mapa, ns, ms] = easylomb(t, thetas, phis, sig, f, ...
	'nn', 15, 'mm', 15, 'dnm', 1, 'plot', 1);


function sig = makesig(t, phis, thetas, modes)
	sig = zeros(length(phis), length(t));
	for i = 1:length(phis)
		tsig = zeros(length(t), 1);
		for j = 1:size(modes, 1)
			A = modes(j, 1);
			w = 2*pi*modes(j, 2);
			m = modes(j, 3);
			n = modes(j, 4);
			tsig = tsig + A*exp(1i*(w*t - n*phis(i) - m*thetas(i)))';
		end
		sig(i, :) = real(tsig);
	end
end


function modes = makemodes(nmodes, fmax, nmmax)
	amp = 10*rand(nmodes, 1) + 10i*rand(nmodes, 1);
	f   = fmax*rand(nmodes, 1);
	n   = round(2*nmmax*rand(nmodes, 1) - nmmax);
	m   = round(2*nmmax*rand(nmodes, 1) - nmmax);
	modes = [amp, f, m, n];
	modes = sort(modes, 'descend', 'ComparisonMethod', 'abs');
end