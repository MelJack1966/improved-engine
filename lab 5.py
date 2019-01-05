def kinetic_energy(mass,velocity):
    return 0.5 * mass * velocity**2

def main():
    activate = input('Do you wish to calulate mass and velocity to kinetic energy? Enter yes or no: ')
    while activate == 'yes':
        mass = float(input('Enter the mass of the object: '))
        velocity = float(input('Enter the velocity of the object: '))
        kineticEnergy = kinetic_energy(mass,velocity)
        print('The kintic energy is ', kineticEnergy)
        activate = input('Do you wish to calulate mass and velocity to kinetic energy? Enter yes or no: ')
main()
