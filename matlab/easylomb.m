function [mapa, ns, ms] = easylomb(time, thetas, phis, signal, f, varargin)
%
%	Pedro Pons-Villalonga, 2021
%
%	Implementation of the 3-dimensional Lomb periodogram (Zegenhagen, 2006)
%	at the frequency $w to:
%		-nn:dnm:nn
%		-mm:dnm:mm
% 
% It returns a matrix TODO
%	
%	INPUT:
%		Required:
%			time:
%				[vec]			Time array.
%			thetas:
%				[vec]			Array of theta positions of the coils
%			phis:
%				[vec]			Array of phi positions of the coils.
%			signal:
%				[matrix]	Matrix of the signals, in the same order as thetas, phis
%			f:
% 			[float]		Frequency for the periodogram
% 			
% 	OPTIONAL:
% 		nn: 
% 			[int]			Max n.
%									Default: 15
% 		mm:
% 			[int]			Max m
%									Default: 15
% 		dnm:
% 			[float]		Interval between ns and ms.
%									Default: 1
% 		plot:
% 			[bool]	Wether or not to plot the periodogram.
%									Default:0
%
%	OUTPUT:
%		mapa:
%			[matrix]		Matrix of the periodogram at n, m
%		ns:
% 		[vec]				Vector of the ns
% 	ms:
% 		[vec]				Vector of the ms

% Input parsing

	def_dnm = 1;
	def_nn = 15;
	def_mm = 15;
	def_plot = 0;
	
	p = inputParser;
	addParameter(p, 'dnm', def_dnm);
	addParameter(p, 'nn', def_nn);
	addParameter(p, 'mm', def_mm);
	addParameter(p, 'plot', def_plot);
	parse(p, varargin{:});
	
	nn = p.Results.nn;
	mm = p.Results.mm;
	dnm = p.Results.dnm;
	toplot = p.Results.plot;

%	Create ns, ms
	ns = -nn:dnm:nn;
	ms = -mm:dnm:mm;

% Create mapa
	mapa = zeros(length(ms), length(ns));
	
% Calculate periodogram over all ns, ms
	for i = 1:length(ns)
		n = ns(i);
		for j = 1:length(ms)
			m = ms(j);
			mapa(j, i) = lomb3(time, thetas, phis, signal, f, m, n);
		end
	end
	
%	Plot
	if toplot==1
		fig = figure;
		imagesc(ns, ms, mapa);
		set(fig.CurrentAxes, 'YDir', 'normal');
		cbar = colorbar;
		cbar.Label.String = 'P [a.u.]';
		xlabel 'n'
		ylabel 'm'
		axis equal
		axis tight
		grid on;
	end
end

function P = lomb3(t, thetas, phis, signal, f, m, n, varargin)
%
% Pedro Pons-Villalonga, 2021
% 	
% Calculates the 3-dimensional Lomb periodogram at m, n, w.
%
%	INPUT:
%		Required:
%			time:
%				[vec]			Time array.
%			thetas:
%				[vec]			Array of theta positions of the coils
%			phis:
%				[vec]			Array of phi positions of the coils.
%			signal:
%				[matrix]	Matrix of the signals, in the same order as thetas, phis
%			f:
% 			[float]		Frequency for the periodogram
% 		m: 
% 			[int]			m. Poloidal mode number.
% 		n:
% 			[int]			n. Toroidal mode number.
%
%	OUTPUT:
%		P:
%			[float]			Value of the periodogram

%	Input parsing
	def_demean = 0;
	
	p = inputParser;
	addParameter(p, 'demean', def_demean);
	parse(p, varargin{:});
	
	demean = p.Results.demean;

% Frequency check
	w = 2*pi*f;
	if w==0
		error('The frequency cannot be zero')
	end
	
% Subtract mean
	if demean==1
		signal = signal - mean(mean(y));
	end
	
% Find tau
	alpha = repmat(n*phis + m*thetas, 1, length(t)) - w*t;
	
% 	arg = sum(sin(2*alpha), 'all') / sum(cos(2*alpha), 'all');
	tau = 0.5*atan2(sum(sin(2*alpha), 'all'), sum(cos(2*alpha), 'all'));
	alpha = alpha - tau;

% Calculate periodogram
	YY = sum(signal.^2, 'all');
	P = (1/YY)*(sum(signal.*cos(alpha), 'all')^2/sum(cos(alpha).^2, 'all') + ...
							sum(signal.*sin(alpha), 'all')^2/sum(sin(alpha).^2, 'all'));
	
	
	
end
















