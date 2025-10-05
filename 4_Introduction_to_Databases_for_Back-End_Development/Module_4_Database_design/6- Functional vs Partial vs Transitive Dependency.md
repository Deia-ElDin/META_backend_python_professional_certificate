## Functional vs Partial vs Transitive Dependency (Clear Differences)

### Functional Dependency (FD)

- Definition: Attribute(s) X determine attribute Y, written X → Y.
- Intuition: for a given X value, Y is uniquely fixed.
- Example: `PatientID → PatientName`

### Partial Dependency

- Definition: In a table whose primary key is composite (A, B), a non-key attribute depends on only part of the key.
- Symptom: (A, B) is the key, but A → C (C is non-key).
- Example (before): `Patient(PatientID, SlotID) is key; PatientName depends only on PatientID`
- Fix (2NF): move `PatientName` to `Patient(PatientID, PatientName)`; keep (PatientID, SlotID, …) in an appointments table with its own key.

### Transitive Dependency

- Definition: A non-key attribute depends on another non-key attribute: A → B and B → C implies A → C (transitively), where C is non-key.
- Example: `Council → Postcode`, and `SurgeryNumber → Council` ⇒ `SurgeryNumber → Postcode` (via Council).
- Fix (3NF): separate determinant into its own table (e.g., `Council(Council PK, Postcode, …)`) and reference it from `Surgery`.

### Quick comparison

| Type                  | When it occurs                                         | Normal form violated | Typical fix                                          |
| --------------------- | ------------------------------------------------------ | -------------------- | ---------------------------------------------------- |
| Functional dependency | Always present; defines keys and determinants          | —                    | Identify correct keys and determinants               |
| Partial dependency    | Non-key depends on subset of a composite primary key   | 2NF                  | Split tables so non-keys depend on full key          |
| Transitive dependency | Non-key depends on another non-key (via a determinant) | 3NF                  | Factor determinant into separate table and reference |

### Mini refactors (SQL sketches)

Partial → 2NF:

```sql
-- Before: Patient(PatientID, SlotID) is key; PatientName depends only on PatientID
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

Transitive → 3NF:

```sql
-- Council determines Postcode; Surgery references Council
CREATE TABLE Council (
  Council VARCHAR(20) PRIMARY KEY,
  Region VARCHAR(20),
  Postcode VARCHAR(10)
);

CREATE TABLE Surgery (
  SurgeryNumber INT PRIMARY KEY,
  Council VARCHAR(20) NOT NULL,
  FOREIGN KEY (Council) REFERENCES Council(Council)
);
```
