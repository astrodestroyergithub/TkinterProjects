from tkinter import *

root = Tk()

root.geometry("1200x890")
root.title("Medical Brain - AstroDestroyer")

f0 = Frame()
f0.pack()

f1 = Frame(bg="light grey", width=642, height=698, borderwidth=7, relief=SUNKEN)
f1.pack(side=LEFT, anchor="nw", padx=10)

f2 = Frame(bg="light grey", width=642, height=698, borderwidth=7, relief=SUNKEN)
f2.pack(side=LEFT, anchor="nw", padx=10)

label0 = Label(f0, text="Medical Brain Application", font="helvetica 26 bold")
label0.pack(pady=2)


# Patient details heading
label1 = Label(f0, text="Patient details", fg="black", font="roboto 17 bold", padx=295, pady=5, borderwidth=7, relief=SUNKEN)
label1.pack(side=LEFT, padx=10, pady=10)

# Doctor details heading
label2 = Label(f0, text="Doctor details", fg="black", font="roboto 17 bold", padx=112, pady=5, borderwidth=7, relief=SUNKEN)
label2.pack(side=LEFT, padx=10, pady=10)


# Enter the patient's name
patient_name = Label(f1, text="Name:", font="roboto 15")
patient_name.grid(row=0, column=0, padx=20, pady=5)
patient_nameentry = Entry(f1, font="roboto 15").grid(row=0, column=1, padx=20, pady=5)

# Enter the patient's date of birth
patient_dob = Label(f1, text="Date of Birth:", font="roboto 15")
patient_dob.grid(row=1, column=0, padx=20, pady=5)
patient_dobentry = Entry(f1, font="roboto 15").grid(row=1, column=1, padx=20, pady=5)

# Enter the patient's address
patient_address = Label(f1, text="Address:", font="roboto 15")
patient_address.grid(row=2, column=0, padx=20, pady=5)
patient_addressentry = Entry(f1, font="roboto 15").grid(row=2, column=1, padx=20, pady=5)

# Enter the patient's sex
patient_sex = Label(f1, text="Sex:", font="roboto 15")
patient_sex.grid(row=3, column=0, padx=20, pady=5)
patient_sexentry = Entry(f1, font="roboto 15").grid(row=3, column=1, padx=20, pady=5)

# Enter the patient's city
patient_city = Label(f1, text="City:", font="roboto 15")
patient_city.grid(row=4, column=0, padx=20, pady=5)
patient_cityentry = Entry(f1, font="roboto 15").grid(row=4, column=1, padx=20, pady=5)

# Enter the patient's state
patient_state = Label(f1, text="State:", font="roboto 15")
patient_state.grid(row=5, column=0, padx=20, pady=5)
patient_stateentry = Entry(f1, font="roboto 15").grid(row=5, column=1, padx=20, pady=5)

# Enter the patient's email
patient_email = Label(f1, text="Email:", font="roboto 15")
patient_email.grid(row=6, column=0, padx=20, pady=5)
patient_emailentry = Entry(f1, font="roboto 15").grid(row=6, column=1, padx=20, pady=5)

# Enter the patient's phone no.
patient_phone = Label(f1, text="Phone:", font="roboto 15")
patient_phone.grid(row=7, column=0, padx=20, pady=5)
patient_phoneentry = Entry(f1, font="roboto 15").grid(row=7, column=1, padx=20, pady=5)

# Enter the patient's occupation
patient_occupation = Label(f1, text="Occupation:", font="roboto 15")
patient_occupation.grid(row=8, column=0, padx=20, pady=5)
patient_occupationentry = Entry(f1, font="roboto 15").grid(row=8, column=1, padx=20, pady=5)

# Enter the patient's height
height = Label(f1, text="Height (in Cms):", font="roboto 15")
height.grid(row=9, column=0, padx=20, pady=5)
heightentry = Entry(f1, font="roboto 15").grid(row=9, column=1, padx=20, pady=5)

# Enter the patient's weight
weight = Label(f1, text="Weight (in Kgs):", font="roboto 15")
weight.grid(row=10, column=0, padx=20, pady=5)
weightentry = Entry(f1, font="roboto 15").grid(row=10, column=1, padx=20, pady=5)

# Enter the patient's pulse
pulse = Label(f1, text="Pulse:", font="roboto 15")
pulse.grid(row=11, column=0, padx=20, pady=5)
pulseentry = Entry(f1, font="roboto 15").grid(row=11, column=1, padx=20, pady=5)

# Enter the patient's BP
bp = Label(f1, text="BP (Blood Pressure):", font="roboto 15")
bp.grid(row=12, column=0, padx=20, pady=5)
bpentry = Entry(f1, font="roboto 15").grid(row=12, column=1, padx=20, pady=5)

# Enter the patient's blood group
bloodgroup = Label(f1, text="Blood group:", font="roboto 15")
bloodgroup.grid(row=13, column=0, padx=20, pady=5)
bloodgroupentry = Entry(f1, font="roboto 15").grid(row=13, column=1, padx=20, pady=5)

# Enter the patient's eye-sight
sight = Label(f1, text="Sight:", font="roboto 15")
sight.grid(row=14, column=0, padx=20, pady=5)
sightentry = Entry(f1, font="roboto 15").grid(row=14, column=1, padx=20, pady=5)

# other patient details
allergies = Label(f1, text="History of Allergy if any:", font="roboto 15")
allergies.grid(row=15, column=0, padx=20, pady=5)
allergiesentry = Entry(f1, font="roboto 15").grid(row=15, column=1, padx=20, pady=5)

medicalillness = Label(f1, text="History of Medical illness if any:", font="roboto 15")
medicalillness.grid(row=16, column=0, padx=20, pady=5)
medicalillnessentry = Entry(f1, font="roboto 15").grid(row=16, column=1, padx=20, pady=5)

hospitalization = Label(f1, text="History of Hospitalization/previous surgeries if any:", font="roboto 15")
hospitalization.grid(row=17, column=0, padx=20, pady=5)
hospitalizationentry = Entry(f1, font="roboto 15").grid(row=17, column=1, padx=20, pady=5)

hospitalization = Label(f1, text="History of Current Medication for any illness:", font="roboto 15")
hospitalization.grid(row=18, column=0, padx=20, pady=5)
hospitalizationentry = Entry(f1, font="roboto 15").grid(row=18, column=1, padx=20, pady=5)



# Enter the doctor's name
doctor_name = Label(f2, text="Name:", font="roboto 15")
doctor_name.grid(row=0, column=0, padx=20, pady=5)
doctor_nameentry = Entry(f2, font="roboto 15").grid(row=0, column=1, padx=20, pady=5)

# Enter the doctor's address
doctor_address = Label(f2, text="Address:", font="roboto 15")
doctor_address.grid(row=2, column=0, padx=20, pady=5)
doctor_addressentry = Entry(f2, font="roboto 15").grid(row=2, column=1, padx=20, pady=5)

# Enter the doctor's sex
doctor_sex = Label(f2, text="Sex:", font="roboto 15")
doctor_sex.grid(row=3, column=0, padx=20, pady=5)
doctor_sexentry = Entry(f2, font="roboto 15").grid(row=3, column=1, padx=20, pady=5)

# Enter the doctor's city
doctor_city = Label(f2, text="City:", font="roboto 15")
doctor_city.grid(row=4, column=0, padx=20, pady=5)
doctor_cityentry = Entry(f2, font="roboto 15").grid(row=4, column=1, padx=20, pady=5)

# Enter the doctor's state
doctor_state = Label(f2, text="State:", font="roboto 15")
doctor_state.grid(row=5, column=0, padx=20, pady=5)
doctor_stateentry = Entry(f2, font="roboto 15").grid(row=5, column=1, padx=20, pady=5)

# Enter the doctor's email
doctor_email = Label(f2, text="Email:", font="roboto 15")
doctor_email.grid(row=6, column=0, padx=20, pady=5)
doctor_emailentry = Entry(f2, font="roboto 15").grid(row=6, column=1, padx=20, pady=5)

# Enter the doctor's phone no.
doctor_phone = Label(f2, text="Phone:", font="roboto 15")
doctor_phone.grid(row=7, column=0, padx=20, pady=5)
doctor_phoneentry = Entry(f2, font="roboto 15").grid(row=7, column=1, padx=20, pady=5)

# Something else to be added here


root.mainloop()
