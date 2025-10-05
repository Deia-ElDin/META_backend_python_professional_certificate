## Data Normalization (1NF, 2NF, 3NF) — Simple Guide

Goal: reduce duplication, avoid update/insert/delete anomalies, and make querying simpler.

### Unnormalized example (simplified)

Mixed attributes and repeating groups (doctor, patient, surgery, costs) in one wide table.

```sql
CREATE TABLE SurgeryRaw (
  DoctorID VARCHAR(10), DoctorName VARCHAR(50), Region VARCHAR(20),
  PatientID VARCHAR(10), PatientName VARCHAR(50),
  SurgeryNumber INT, Council VARCHAR(20), Postcode VARCHAR(10),
  SlotID VARCHAR(10), TotalCost DECIMAL(10,2)
);
```

### First Normal Form (1NF)

- Rule: each cell holds a single atomic value; no repeating groups.
- Action: move patient-related repeating data into a separate table; use a composite key for uniqueness.

```sql
CREATE TABLE PatientRaw1NF (
  PatientID VARCHAR(10) NOT NULL,
  PatientName VARCHAR(50),
  SlotID VARCHAR(10) NOT NULL,
  TotalCost DECIMAL(10,2),
  CONSTRAINT PK_PatientRaw1NF PRIMARY KEY (PatientID, SlotID)
);
```

Also split remaining attributes into focused tables (e.g., Doctor, Surgery) to remove repeats:

```sql
CREATE TABLE Doctor (
  DoctorID VARCHAR(10) PRIMARY KEY,
  DoctorName VARCHAR(50)
);

CREATE TABLE Surgery (
  SurgeryNumber INT PRIMARY KEY,
  Region VARCHAR(20),
  Council VARCHAR(20),
  Postcode VARCHAR(10)
);
```

### Second Normal Form (2NF)

- Rule: no partial dependency on part of a composite key.
- Problem: in `PatientRaw1NF(PatientID, SlotID)`, `PatientName` depends only on `PatientID`, and `TotalCost` may depend only on `SlotID`.
- Action: split into separate tables so non-key columns depend on the whole key of their table.

```sql
CREATE TABLE Patient (
  PatientID VARCHAR(10) PRIMARY KEY,
  PatientName VARCHAR(50)
);

CREATE TABLE Appointment (
  AppointmentID INT PRIMARY KEY,
  PatientID VARCHAR(10) NOT NULL,
  SlotID VARCHAR(10) NOT NULL,
  TotalCost DECIMAL(10,2),
  FOREIGN KEY (PatientID) REFERENCES Patient(PatientID)
);
```

### Third Normal Form (3NF)

- Rule: no transitive dependency (non-key attribute depending on another non-key attribute).
- Problem: in `Surgery`, `Postcode` depends on `Council` (both non-keys).
- Action: move the determinant into its own table and reference it.

```sql
CREATE TABLE Council (
  Council VARCHAR(20) PRIMARY KEY,
  Region VARCHAR(20)
);

CREATE TABLE Surgery3NF (
  SurgeryNumber INT PRIMARY KEY,
  Council VARCHAR(20) NOT NULL,
  Postcode VARCHAR(10) NOT NULL,
  FOREIGN KEY (Council) REFERENCES Council(Council)
);
```

Result: tables are in 3NF — reduced duplication and clearer relationships.

### Example tables (at each step)

#### Unnormalized (mixed, repeating)

| DoctorID | DoctorName | Region      | PatientID | PatientName | SurgeryNumber | Council | Postcode | SlotID | TotalCost |
| -------- | ---------- | ----------- | --------- | ----------- | ------------- | ------- | -------- | ------ | --------- |
| D1       | Karl       | West London | P1        | Rami        | 3             | Harrow  | HA9SDE   | A1     | 1500.00   |
| D1       | Karl       | East London | P4        | Kamel       | 4             | Hackney | E1 6AW   | A2     | 2500.00   |

#### 1NF (atomic values, no repeating groups)

Patient (composite PK: PatientID, SlotID)

| PatientID | PatientName | SlotID | TotalCost |
| --------- | ----------- | ------ | --------- |
| P1        | Rami        | A1     | 1500.00   |
| P2        | Kim         | A2     | 1200.00   |

Doctor

| DoctorID | DoctorName |
| -------- | ---------- |
| D1       | Karl       |
| D2       | Mark       |

Surgery

| SurgeryNumber | Region      | Council | Postcode |
| ------------- | ----------- | ------- | -------- |
| 3             | West London | Harrow  | HA9SDE   |
| 4             | East London | Hackney | E1 6AW   |

#### 2NF (no partial dependency on a composite key)

Patient (single-column PK)

| PatientID | PatientName |
| --------- | ----------- |
| P1        | Rami        |
| P2        | Kim         |

Appointment (each row identified by its own key)

| AppointmentID | PatientID | SlotID | TotalCost |
| ------------- | --------- | ------ | --------- |
| 101           | P1        | A1     | 1500.00   |
| 102           | P2        | A2     | 1200.00   |

#### 3NF (no transitive dependency)

Council (determinant separated)

| Council | Region      |
| ------- | ----------- |
| Harrow  | West London |
| Hackney | East London |

Surgery (references Council)

| SurgeryNumber | Council | Postcode |
| ------------- | ------- | -------- |
| 3             | Harrow  | HA9SDE   |
| 4             | Hackney | E1 6AW   |
