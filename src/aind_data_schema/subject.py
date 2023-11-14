""" schema for mostly mouse metadata """

from datetime import date as date_type
from datetime import time
from enum import Enum
from typing import Final, List, Literal, Optional

from pydantic import Field

from aind_data_schema.base import AindCoreModel, AindModel
from aind_data_schema.models.institution import INSTITUTIONS
from aind_data_schema.models.pid_names import PIDName
from aind_data_schema.models.species import SPECIES


class Sex(str, Enum):
    """Subject sex name"""

    FEMALE = "Female"
    MALE = "Male"


class BackgroundStrain(str, Enum):
    """Animal background strain name"""

    BALB_c = "BALB/c"
    C57BL_6J = "C57BL/6J"


class HomeCageEnrichment(str, Enum):
    """Materials provided in animal home cage"""

    NONE = "None"
    PLASTIC_SHELTER = "Plastic shelter"
    PLASTIC_TUBE = "Plastic tube"
    RUNNING_WHEEL = "Running wheel"
    OTHER = "Other"


class LightCycle(AindModel):
    """Description of vivarium light cycle times"""

    lights_on_time: time = Field(
        ...,
        description="Time in UTC that lights were turned on",
        title="Lights on time",
    )
    lights_off_time: time = Field(
        ...,
        description="Time in UTC that lights were turned off",
        title="Lights off time",
    )


class WellnessReport(AindModel):
    """Wellness report on animal health"""

    date: date_type = Field(..., title="Date")
    report: str = Field(..., title="Report")


class MgiAlleleId(AindModel):
    """Mouse Genome Informatics IDs for genotype alleles"""

    allele_name: str = Field(..., title="Name")
    mgi_id: str = Field(..., title="MGI ID")


class Housing(AindModel):
    """Description of subject housing"""

    cage_id: Optional[str] = Field(None, title="Cage ID")
    room_id: Optional[str] = Field(None, title="Room ID")
    light_cycle: Optional[LightCycle] = Field(None, title="Light cycle")
    home_cage_enrichment: List[HomeCageEnrichment] = Field([], title="Home cage enrichment")
    cohoused_subjects: List[str] = Field(
        [],
        title="Co-housed subjects",
        description="List of IDs of other subjects housed in same cage",
    )


class Subject(AindCoreModel):
    """Description of a subject of data collection"""

    _DESCRIBED_BY_URL: Final = AindCoreModel._DESCRIBED_BY_BASE_URL + "aind_data_schema/subject.py"

    describedBy: str = Field(_DESCRIBED_BY_URL, json_schema_extra={"const": True})
    schema_version: Literal["0.5.0"] = Field("0.5.0")
    species: SPECIES = Field(..., title="Species")
    subject_id: str = Field(
        ...,
        description="Unique identifier for the subject. If this is not a Allen LAS ID, indicate this in the Notes.",
        title="Subject ID",
    )
    sex: Sex = Field(..., title="Sex")
    date_of_birth: date_type = Field(..., title="Date of birth")
    genotype: str = Field(
        ...,
        description="Genotype of the animal providing both alleles",
        title="Genotype",
    )
    mgi_allele_ids: List[MgiAlleleId] = Field([], title="MGI allele ids")
    background_strain: Optional[BackgroundStrain] = Field(None, title="Background strain")
    source: Optional[INSTITUTIONS] = Field(
        None,
        description="If the subject was not bred in house, where was it acquired from.",
        title="Source",
    )
    rrid: Optional[PIDName] = Field(
        None,
        description="RRID of mouse if acquired from supplier",
        title="RRID",
    )
    restrictions: Optional[str] = Field(
        None,
        description="Any restrictions on use or publishing based on subject source",
        title="Restrictions",
    )
    breeding_group: Optional[str] = Field(None, title="Breeding Group")
    maternal_id: Optional[str] = Field(None, title="Maternal specimen ID")
    maternal_genotype: Optional[str] = Field(None, title="Maternal genotype")
    paternal_id: Optional[str] = Field(None, title="Paternal specimen ID")
    paternal_genotype: Optional[str] = Field(None, title="Paternal genotype")
    wellness_reports: List[WellnessReport] = Field([], title="Wellness Report")
    housing: Optional[Housing] = Field(None, title="Housing")
    notes: Optional[str] = Field(None, title="Notes")
