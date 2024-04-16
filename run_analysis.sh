mkdir -p results
python bin/calc_fractal.py 3 results/data.dat
python bin/fig1.py
python bin/calc_fractal.py 5 results/data.dat
python bin/fig2.py
python bin/calc_fractal.py 6 results/data.dat
python bin/fig3.py
python bin/fig4.py