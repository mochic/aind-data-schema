""" schema for various Procedures """

from __future__ import annotations

from datetime import date, time
from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel, Field


class ProtectiveMaterial(Enum):
    """material applied post-craniotomy"""

    Duragel = "Duragel"
    SORTA_clear = "SORTA-clear"
    Kwik_Cast = "Kwik-Cast"
    Other = "Other - see notes"


class Craniotomy(BaseModel):
    """description of the craniotomy"""

    date: date = Field(..., title="Date")
    experimenter_full_name: str = Field(
        ...,
        description="First and last name of the experimenter.",
        title="Experimenter full name",
    )
    craniotomy_protocol_id: str = Field(..., title="Craniotomy protocol ID")
    craniotomy_coordinates_ml: float = Field(
        ..., title="Craniotomy coordinate ML (mm)"
    )
    craniotomy_coordinates_ap: float = Field(
        ..., title="Craniotomy coordinates AP (mm)"
    )
    craniotomy_size: float = Field(..., title="Craniotomy size (mm)")
    implant_part_number: Optional[str] = Field(
        None, title="Implant part number"
    )
    dura_removed: Optional[bool] = Field(None, title="Dura removed")
    protective_material: Optional[ProtectiveMaterial] = Field(
        None, title="Protective material"
    )
    notes: Optional[str] = Field(None, title="Notes")


class HeadframeMaterial(Enum):
    """headframe materials"""

    Titanium = "Titanium"
    Steel = "Steel"


class WellType(Enum):
    """TODO"""

    A = "A"
    B = "B"


class Headframe(BaseModel):
    """description of headframe procedure"""

    date: date = Field(..., title="Date")
    experimenter_full_name: str = Field(
        ...,
        description="First and last name of the experimenter.",
        title="Experimenter full name",
    )
    headframe_protocol_id: str = Field(..., title="Headframe protocol ID")
    headframe_part_number: str = Field(..., title="Headframe part number")
    headframe_material: HeadframeMaterial = Field(
        ..., title="Headframe material"
    )
    well_part_number: Optional[str] = Field(None, title="Well part number")
    well_type: Optional[WellType] = Field(None, title="Well type")
    notes: Optional[str] = Field(None, title="Notes")


class InjectionHemisphere(Enum):
    """brain hemisphere targeted by injection"""

    left = "left"
    right = "right"


class NanojectInjection(BaseModel):
    """description of nanoject injection"""

    injection_type: str = Field("Nanoject", title="Injection type", const=True)
    injection_volume: float = Field(..., title="Injection volume (nL)")


class IontophoresisInjection(BaseModel):
    """description of nanoject injection"""

    injection_type: str = Field(
        "Iontophoresis", title="Injection type", const=True
    )
    injection_current: float = Field(..., title="Injection current (uA)")
    alternating_current: str = Field(..., title="Alternating current")


class Injection(BaseModel):
    """general description of injection procedure"""

    date: date = Field(..., title="Date")
    experimenter_full_name: str = Field(
        ...,
        description="First and last name of the experimenter.",
        title="Experimenter full name",
    )
    injection_protocol_id: str = Field(..., title="Injection protocol ID")
    injection_hemisphere: Optional[InjectionHemisphere] = Field(
        None, title="Injection hemisphere"
    )
    injection_coordinate_ml: float = Field(
        ..., title="Injection coordinate ML (mm)"
    )
    injection_coordinate_ap: float = Field(
        ..., title="Injection coordinate AP (mm)"
    )
    injection_coordinate_depth: float = Field(
        ..., title="Injection coodinate depth (mm)"
    )
    injection_angle: float = Field(..., title="Injection angle (deg)")
    injection_virus: str = Field(..., title="Injection virus")
    injection_virus_id: Optional[str] = Field(None, title="Injection virus ID")
    injection_duration: time = Field(..., title="Injection duration")
    notes: Optional[str] = Field(None, title="Notes")
    injection_class: Union[NanojectInjection, IontophoresisInjection]


class MriScanSequence(Enum):
    """MRI scan sequence"""

    RARE = "RARE"


class ScannerLocation(Enum):
    """location of scanner"""

    UW_SLU = "UW SLU"
    Fred_Hutch = "Fred Hutch"


class MagneticStrength(Enum):
    """strength of magnet"""

    integer_7 = 7
    integer_14 = 14


class MriScan(BaseModel):
    """information about MRI scan"""

    date: date = Field(..., title="Date")
    experimenter_full_name: str = Field(
        ...,
        description="First and last name of the experimenter.",
        title="Experimenter full name",
    )
    scan_sequence: MriScanSequence = Field(..., title="Scan sequence")
    scanner_location: Optional[ScannerLocation] = Field(
        None, title="Scanner location"
    )
    magnetic_strength: Optional[MagneticStrength] = Field(
        None, title="Magnetic strength (T)"
    )
    resolution: float = Field(..., title="Resolution")
    protocol_id: str = Field(..., title="Protocol ID")


class TissuePrepName(Enum):
    """type of tissue prep"""

    Perfusion = "Perfusion"
    Fixation = "Fixation"
    Double_delipidation = "Double delipidation"
    DCM_delipidation = "DCM delipidation"
    Immunostaining = "Immunostaining"
    Gelation = "Gelation"


class TissuePrep(BaseModel):
    """information about tissue prep procedure"""

    name: TissuePrepName = Field(..., title="Name")
    date_started: date = Field(..., title="Date started")
    date_ended: Optional[date] = Field(None, title="Date ended")
    experimenter_full_name: Optional[str] = Field(
        None,
        description="First and last name of the experimenter.",
        title="Experimenter full name",
    )
    protocol_id: str = Field(..., title="Protocol ID")
    notes: Optional[str] = None


class TrainingProtocol(BaseModel):
    """information about training procedures"""

    training_protocol_id: str = Field(..., title="Training protocol ID")
    training_protocol_start_date: date = Field(
        ..., title="Training protocol start date"
    )
    training_protocol_end_date: Optional[date] = Field(
        None, title="Training protocol end date"
    )
    notes: Optional[str] = Field(None, title="Notes")


class ProbeName(Enum):
    """name of probe"""

    Probe_A = "Probe A"
    Probe_B = "Probe B"
    Probe_C = "Probe C"


class FerruleMaterial(Enum):
    """probe material"""

    Ceramic = "Ceramic"
    Stainless_steel = "Stainless steel"


class Probe(BaseModel):
    """description of probe"""

    name: ProbeName = Field(..., title="Name")
    manufacturer: str = Field(..., title="Manufacturer")
    part_number: str = Field(..., title="Part number")
    core_diameter: float = Field(..., title="Core diameter (um)")
    numerical_aperture: float = Field(..., title="Numerical aperture")
    ferrule_material: Optional[FerruleMaterial] = Field(
        None, title="Ferrule material"
    )
    targeted_structure: str = Field(..., title="Targeted structure")
    stereotactic_coordinate_ap: float = Field(
        ..., title="Stereotactic coordinate A/P (mm)"
    )
    stereotactic_coordinate_ml: float = Field(
        ..., title="Stereotactic coodinate M/L (mm)"
    )
    stereotactic_coordinate_dv: float = Field(
        ..., title="Stereotactic coordinate D/V (mm)"
    )
    angle: float = Field(..., title="Angle (deg)")
    notes: Optional[str] = Field(None, title="Notes")


class Implant(BaseModel):
    """description of implant procedure"""

    date: date = Field(..., title="Date")
    experimenter_full_name: str = Field(
        ...,
        description="First and last name of the experimenter.",
        title="Experimenter full name",
    )
    probes: List[Probe] = Field(..., title="Probes", unique_items=True)


class WaterRestriction(BaseModel):
    """description of water description protocol"""

    protocol_id: Optional[str] = Field(
        None, title="Water restriction protocol number"
    )
    start_date: Optional[date] = Field(
        None, title="Water restriction start date"
    )
    end_date: Optional[date] = Field(None, title="Water restriction end date")


class Procedures(BaseModel):
    """description of all procedures applied to subject"""

    describedBy: str = Field(
        "https://github.com/AllenNeuralDynamics/aind-data-schema/blob/main/src/aind-data-schema/procedures.py",
        description="The URL reference to the schema.",
        title="Described by",
        const=True,
    )
    schema_version: str = Field(
        "0.3.0", description="schema version", title="Version", const=True
    )
    specimen_id: str = Field(
        ...,
        description="Unique identifier for the subject. If this is not a Allen LAS ID, indicate this in the Notes.",
        title="Specimen ID",
    )
    headframes: Optional[List[Headframe]] = Field(
        None, title="Headframes", unique_items=True
    )
    craniotomies: Optional[List[Craniotomy]] = Field(
        None, title="Craniotomies", unique_items=True
    )
    mri_scans: Optional[List[MriScan]] = Field(
        None, title="MRI scans", unique_items=True
    )
    injections: Optional[List[Injection]] = Field(
        None, title="Injections", unique_items=True
    )
    fiber_implants: Optional[List[Implant]] = Field(
        None, title="Fiber implants", unique_items=True
    )
    water_restriction: Optional[WaterRestriction] = Field(
        None, title="Water restriction"
    )
    training_protocols: Optional[List[TrainingProtocol]] = Field(
        None, title="Training protocols", unique_items=True
    )
    tissue_preparations: Optional[List[TissuePrep]] = Field(
        None, title="Tissue preparations", unique_items=True
    )
    notes: Optional[str] = Field(None, title="Notes")
