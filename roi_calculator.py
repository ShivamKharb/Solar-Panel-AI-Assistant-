# roi_calculator.py

import numpy as np

def calculate_area(mask, pixel_size=0.005):
    # Count white pixels in mask (255)
    return np.sum(mask == 255) * pixel_size


def calculate_roi(data):
    try:
        area = float(data.get("usable_area_m2", 0))
        if area <= 0:
            raise ValueError("Usable area must be a positive number.")

        panel_area = 1.6
        efficiency = 0.18
        sunlight_hours_per_year = 1500
        panel_cost_inr = 20750
        savings_per_kwh_inr = 10

        num_panels = int(area // panel_area)
        annual_energy = num_panels * efficiency * sunlight_hours_per_year
        total_cost = num_panels * panel_cost_inr
        annual_savings = annual_energy * savings_per_kwh_inr
        payback = total_cost / annual_savings if annual_savings else float('inf')

        return {
            "Number of Panels": num_panels,
            "Estimated Annual Output (kWh)": round(annual_energy, 2),
            "Estimated Installation Cost (INR)": round(total_cost, 2),
            "Annual Savings (INR)": round(annual_savings, 2),
            "Payback Period (Years)": round(payback, 1),
            "Recommended Panel Type": "Monocrystalline"
        }

    except Exception as e:
        return {"error": str(e)}
