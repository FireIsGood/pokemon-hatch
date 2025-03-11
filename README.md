# Pokemon Hatch

Hatch Pokemon from your terminal!

## Running

To run the program, you first must have the other microservices running in the background.

### Install Microservices

Clone and install [microservice A](https://github.com/sju0214/Random-Pokemon):

```bash
git clone git@github.com:sju0214/Random-Pokemon.git ./microservice-a
cd microservice-a
npm install
cd ..
```

Clone and install [microservice B](https://github.com/FireIsGood/pokemon-hatch-microservice-b):

```bash
git clone git@github.com:FireIsGood/pokemon-hatch-microservice-b.git ./microservice-b
cd microservice-b
npm install
cd ..
```

Clone and install [microservice C](https://github.com/FireIsGood/pokemon-hatch-microservice-c):

```bash
git clone git@github.com:FireIsGood/pokemon-hatch-microservice-c.git ./microservice-c
cd microservice-c
npm install
cd ..
```

Clone and install [microservice D](https://github.com/FireIsGood/pokemon-hatch-microservice-d):

```bash
git clone git@github.com:FireIsGood/pokemon-hatch-microservice-d.git ./microservice-d
cd microservice-d
npm install
cd ..
```

### Run the Main Program

Start up all the microservices. This is most easily done in a separate terminal as to not clog the background processes
of the terminal running the main app.

```bash
cd microservice-a && npm run dev &;cd ..
cd microservice-b && npm run start &;cd ..
cd microservice-c && npm run start &;cd ..
cd microservice-d && npm run start &;cd ..
```

(don't ask...)

If you need to kill the processes, use `fg` and then exit with `C-c`.

```bash
fg
# Use C-c (Ctrl+c), then press enter to make your prompt come back
# repeat until all background processes are killed
```

Once all microservices are started, you must enter a virtual environment and install dependencies for the main program.
The `venv.sh` script is provided to automate setting up your virtual environment.

```bash
# Set up a virtual environment
chmod +x
./venv.sh

# Enable the environment
. ./venv/bin/activate

# Disable the environment (after running the app)
deactivate
```

Finally, you can run the `app.py` file with python 3 or above.

```bash
python3 app.py
```
